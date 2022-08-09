require('dotenv').config();
const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const shortID = require('shortid');
const validUrl = require('valid-url');
const app = express();

// Basic Configuration
const port = process.env.PORT || 3000;

app.use(cors());

app.use('/public', express.static(`${process.cwd()}/public`));
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

app.get('/', function (req, res) {
  res.sendFile(process.cwd() + '/views/index.html');
});

// Your first API endpoint
app.get('/api/hello', function (req, res) {
  res.json({ greeting: 'hello API' });
});

// Connect to the database
mongoose
  .connect(process.env.MONGODB_URI, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  })
  .then(() => {
    console.log('Database connected');
  })
  .catch((error) => {
    console.log('Database connection error');
  });

// URL schema
const urlSchema = new mongoose.Schema({
  longURL: {
    type: String,
    required: true,
    unique: true,
  },
  shortURL: {
    type: String,
    required: true,
    default: shortID.generate,
  },
});

// URL model
const urlModel = mongoose.model('URL', urlSchema);

// Endpoint for shortening the url
app.post('/api/shorturl', async function (req, res) {
  const url = req.body.url;
  const pattern = new RegExp('^((http|https|ftp)://)');
  if (!validUrl.isUri(url) || !pattern.test(url)) {
    return res.json({ error: 'invalid url' });
  }

  let shortURL;
  let doc = await urlModel.findOne({ longURL: url });
  if (doc) {
    shortURL = doc.shortURL;
  } else {
    // Create a new instance
    doc = new urlModel({ longURL: url });

    // Save the recent instance
    await doc.save();
    shortURL = doc.shortURL;
  }

  res.json({ original_url: url, short_url: shortURL });
});

// Endpoint for url directing
app.get('/api/shorturl/:shortURL', async function (req, res) {
  const shortURL = req.params.shortURL;
  const doc = await urlModel.findOne({ shortURL: shortURL });

  if (doc) {
    res.redirect(doc.longURL);
  } else {
    res.json('Not found');
  }
});

app.listen(port, function () {
  console.log(`Listening on port ${port}`);
});
