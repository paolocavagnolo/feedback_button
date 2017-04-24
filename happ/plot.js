const username = "paoloc";
const api_key = "YptCGWZIdb8lA3iEfkHR";

var plotly = require('plotly')(username, api_key);

const Sqlite3 = require('sqlite3');
const db = new Sqlite3.Database('../data/data.sqlite');

// var data = [{x:[0,1,2], y:[3,2,1], type: 'bar'}];
// var layout = {fileopt : "overwrite", filename : "simple-node-example"};

// plotly.plot(data, layout, function (err, msg) {
// 	if (err) return console.log(err);
// 	console.log(msg);
// });

let sql = 'SELECT * FROM risposte';

const params = [];

db.all(sql, params, (err, results) => {
   			
        	if (err) {
            	throw err;
			}

        	set_dati = analizza(results);
});

function analizza( dati ) {
	var domanda = "";
	var set_dati = [];
	var id_domanda = 0;
	
	var text = '{ "employees" : [' +
		'{ "firstName":"John" , "lastName":"Doe" },' +
		'{ "firstName":"Anna" , "lastName":"Smith" },' +
		'{ "firstName":"Peter" , "lastName":"Jones" } ]}';
	var obj = JSON.parse(text);

    for(var k in dati) {
   		console.log(k, dati[k].voto);
   		
   		if ( k>=1 ) { //non fare nulla nel primo caso
   			if (dati[k].domanda == domanda) { //stessa domanda
   				
   			}
   			else { //cambio domanda

   				id_domanda = id_domanda + 1;
   			}
   		}

   		//serve per il check del cambio domanda
   		domanda = dati[k].domanda;
	}



	return set_dati;        

}

