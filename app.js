var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var mongoose = require('mongoose');

app.use(express.static(__dirname+'/client'));
app.use(bodyParser.json());

Dish = require('./models/dishModels');
Restaurant = require('./models/restaurantModels');

//Connect to mongoose
mongoose.connect('mongodb://localhost/menu');
var db = mongoose.connection;

app.get('/', function(req, res){
	res.send("hello world");
});

//To Get All the dishes from database
app.get('/api/dishes', function(req, res){
    var type = req.query.type;
    if(type === undefined){
        Dish.getDishes(function(err,dishes){
            if(err){
                throw err;
            }
            res.json(dishes);
        });
    }
    else{
        Dish.getDishesByType(type ,function(err,dishes){
            if(err){
                throw err;
            }
            res.json(dishes);
        });
    }


});


//Get the dish by id from database
app.get('/api/dishes/:_id', function(req, res){
	Dish.getDishById(req.params._id, function(err, dish){
		if(err){
			throw err;
		}
		res.json(dish);
	});
});



//To Get All the restaurants from database
app.get('/api/restaurants', function(req, res){
    console.log(req.params.type);
	Restaurant.getRestaurants(function(err,restaurants){
		if(err){
			throw err;
		}
		res.json(restaurants);
	});
});


//To Get a Restaurant By id from database
app.get('/api/restaurants/:_id', function(req, res){
	Restaurant.getRestaurantById(req.params._id, function(err,restaurant){
		if(err){
			throw err;
		}
		res.json(restaurant);
	});
});



//To Get a Restaurant By Name from database
app.get('/api/restaurants?{name}', function(req, res){
	Restaurant.getRestaurantById(req.params._id, function(err,restaurant){
		if(err){
			throw err;
		}
		res.json(restaurant);
	});
});

app.listen(3001);
console.log("Running on port 3001");
