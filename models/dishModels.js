var mongoose = require('mongoose');

//Dishes Schema
var dishSchema = mongoose.Schema({
	dishName:{
		type: String,
		required : true
	},
	dishIngredients:{
		type: String,
		required : true
	},
	dishPrice:{
		type: String,
		required : true
	},
    type:{
		type: String,
		required : true
	},
	restaurantName:{
		type: String,
		required : true
	},
	restaurantAddress:{
		type: String,
		required : true
	},
	restaurantEmail:{
		type: String,
		required : true
	},
	restaurantPhone:{
		type: String,
		required : true
	},

	create_date:{
		type: Date,
		default: Date.now
	}	
});

//Dish collection will automeically generate in MongoDB 
var Dish = module.exports = mongoose.model('Dish',dishSchema);

//Get All Dishes
module.exports.getDishes = function(callback, limit){
	Dish.find(callback).limit(limit);
}

//Get Specific Dish by id
module.exports.getDishById = function(id, callback){
	Dish.findById(id, callback);
}

//Get Dishes by type on Main Screen
module.exports.getDishesByType = function(types, callback, limit){
	//console.log("I am here "+type);
    Dish.find({type : types}, callback).limit(limit);
}