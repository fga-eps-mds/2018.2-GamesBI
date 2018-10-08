import requests
import os

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework import permissions
from rest_framework import status
from .utils import login_metabase
from .utils import get_database_id
from .utils import get_table_id
from .utils import MB_URL
from .serializers import IframeSerializer
from .models import Iframe
from rest_framework.authentication import SessionAuthentication
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

DB_NAME = os.environ['DB_NAME']
TABLE_NAME = 'importdata_generaldata'


def get_session_id():
    return login_metabase()

@permission_classes((permissions.AllowAny,))
class DashboardIframes(APIView):
    authentication_classes = (JSONWebTokenAuthentication,
                              SessionAuthentication)

    def create_card_metabase(self, data, header):
        url_card = MB_URL + '/card'
        from pprint import pprint
        card = requests.post(url_card, json=data,
                             headers=header)
        pprint(data)
        if card.status_code == 200:
            return card
        else:
            raise Exception("Could not create the card on metabase")

    def make_card_public(self, id, header):
        url_public_card = MB_URL + '/card/{}/public_link'.format(id)

        public_card = requests.post(url_public_card, headers=header)

        if public_card.status_code == 200:
            return public_card
        else:
            raise Exception("Could not make the card public on metabase")

    def make_visualization_settings(self, request):
        display = request['display']

        if display == "pie":
            data = {
                "pie.metric": request['metric'],
                "pie.dimension": request['dimension']
            }
        elif display == "line":
            data = {
                "graph.dimensions": request['dimension'],
                "graph.metrics": request['metric']
            }
        else:
            data = {}
        return data

    def post(self, request, format=None):
        if Iframe.objects.filter(name=request.data['name']).count() != 0:
            return Response(status=status.HTTP_200_OK)

        session_id = get_session_id()
        database_id = get_database_id(DB_NAME)
        table_name = TABLE_NAME
        table_id = get_table_id(database_id, table_name)
        header = {'Cookie': 'metabase.SESSION_ID=' + session_id}
        data = {
            "name": request.data['name'],
            "display": request.data['display'],
            "dataset_query": {
                "database": database_id,
                "type": "query",
                "query": self.get_query(request.data, table_id)
            },
            "visualization_settings": self.make_visualization_settings(request.data)
        }

        card = self.create_card_metabase(data, header)
        public_card = self.make_card_public(card.json()['id'], header)
        uuid = public_card.json()['uuid']
        iframe_data = {
            "name": request.data['name'],
            "uuid": uuid,
        }
        serializer = IframeSerializer(data=iframe_data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)

    def get_query(self, data, table_id):
        attrs = ['aggregation', 'breakout', 'filter', 'order', 'limit']
        query = { 'source_table': table_id }
        for field in data:
            query_field = 'query' + field
            if query_field in attrs:
                query[field] = data[query_field]

        return query


    def get(self, request, format=None):
        iframe = Iframe.objects.filter(name=request.GET.get('name', ''))[0]
        print(type(iframe))
        data = {
            'name': iframe.name,
            'uuid': iframe.uuid
        }
        from pprint import pprint 
        pprint(data)

        return Response(status=status.HTTP_200_OK, data=data)

