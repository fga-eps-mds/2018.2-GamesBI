db.createUser(
    {
      user: 'user',
      pwd: 'pass',
      roles: [
         { role: "dbOwner", db: 'mongo' }
      ]
    }
,
    {
        w: "majority",
        wtimeout: 5000
    }
);
db.createCollection('mongo');
