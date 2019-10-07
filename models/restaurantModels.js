var mongoose = require('mongoose');

//Restaurants Schema
var restaurantSchema = mongoose.Schema({
	name:{
		type: String,
		required : true
	},
	address:{
		type: String,
		required : true
	},
	phone:{
		type: String,
		required : true
	},
	email:{
		type: String,
		required : true
	},
	create_date:{
		type: Date,
		default: Date.now
	}	
});

var Restaurant = module.exports = mongoose.model('Restaurant',restaurantSchema);

//Get All Restaurants
module.exports.getRestaurants = function(callback, limit){
	Restaurant.find(callback).limit(limit);
}

//Get Specific Restaurant by id
module.exports.getRestaurantById = function(id, callback){
	Restaurant.findById(id, callback);
}


//Find by name
module.exports.getRestaurantByName = function(rName, limit){
    var query = {name : rnNme};
	Restaurant.find(query, callback);
}