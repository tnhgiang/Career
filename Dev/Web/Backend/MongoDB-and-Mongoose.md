[# MongoDB and Mongoose](https://www.freecodecamp.org/learn/back-end-development-and-apis/#mongodb-and-mongoose)

- _MongoDB_ is a JSON-like document and non-relational database. _MongoDB_ stores all associated data within one record, instead of storing it across many preset tables as in a traditional SQL database.
- _Mongoose_ is an [Object Data Modeling](https://www.mongodb.com/developer/article/mongoose-versus-nodejs-driver/#object-data-modeling-in-mongodb) (ODM) library for _MongoDB_. _Mongoose_ makes it easier to work with _MongoDB_, also allows us to create _schemas_ which prevents we accidentally save the wrong type of data and cause bugs later.

## Create a Model

- A _Mongoose model_ is a wrapper on the _Mongoose schema_.
- Each _Mongoose schema_ maps to a MongoDB collection and it defines the structure of the document (default values, validators, etc...).
- _Mongoose model_ provides an interface to the database (creating, querying, updating, deleting records, etc ...)

- Creating a _Mongoose model_ consists of 3 steps:

1. Referencing Mongoose

```js
let mongoose = require('mongoose');
```

2. Defining the schema

```js
let emailSchema = new mongoose.Schema({
  email: {
    type: String,
    required: true,
    unique: true,
    lowercase: true,
  },
});
```

3. Creating a model

```js
// Email is the collection name
let EmailModel = mongoose.model('Email', 'emailSchema');
```

## Create a record

- Create an instance of the email model and save it to the database

```js
let msg = new EmailModel({
  email: 'ADA.LOVELACE@GMAIL.COM',
});

msg
  .save()
  .then((doc) => {
    console.log(doc);
  })
  .catch((err) => {
    console.error(err);
  });
```

## Create multiple records

```js
const emailList = [
  { email: 'email1@gmail.com' },
  { email: 'email2@gmail.com' },
];
EmailModel.create(emailList)
  .then((doc) => console.log(doc))
  .catch((err) => console.error(err));
```

## Find records

```js
EmailModel.find({
  email: 'ada.lovelace@gmail.com', // search query
})
  .then((doc) => {
    console.log(doc);
  })
  .catch((err) => {
    console.error(err);
  });
```

## Find one record

- _Model.findOne()_ behaves like _Model.find()_, but it returns only document (not an array), even if there are multiple items. It is especially useful when searching by properties that you have declared as unique.
- _Model.findById()_ will search a record by its _\_id_. It equivalents to _Model.findOne()_
- _Model.findOne()_ is a `potentially-null single document`

## Update one record

- _Model.findOneAndUpdate()_ will help document updating. By default, it returns unmodified object. To return the updated document, we need set `{new: true}`.

## Remove one record

- _Model.findOneAndUpdate()_ will help document removing.

## Remove many records

- _Model.remove()_ will remove records that meet the certain criteria.

## Chain search query helpers

- A mongoose query can be executed in one of two ways:

  - `callback`
  - `.then()`

- With the chaining syntax, query helper functions can be chained together to build up a query. And, it will be executed when the last chained function is `.exec()` with `callback` or `.then()`

```js
Person.find({ occupation: /host/ })
  .where('name.last')
  .equals('Ghost')
  .where('age')
  .gt(17)
  .lt(66)
  .where('likes')
  .in(['vaporizing', 'talking'])
  .limit(10)
  .sort('-occupation')
  .select('name occupation')
  .exec(callback);
```
