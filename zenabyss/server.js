var  fs = require("fs"),

// express software
  express = require("express"),
  morgan = require('morgan'),
  bp = require("body-parser"),
  cookieParser = require("cookie-parser"),
// mysql software
  mysql = require("mysql"),
  connect = require("connect"),
// hashing software
bcrypt = require("bcrypt"),
  md5 = require('md5'),
 saltRoundsHashes = 12;

// modules
var sqlcheck = require('./sqlcheck')
var sqlcomplete = require('./sqlcomplete')
var sqldb = require('./sqldb')
var userAuth = require('./userAuth')

//steps
// grab user input
// hash it
// check if user exist
// if so send error to client
// if not send to database
// then send them client login info
