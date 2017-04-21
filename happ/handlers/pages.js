exports.home = function (request, reply) {

    const domanda = [{
        testo: 'Era buono il cibo in mensa oggi',
    }];


    reply.view('index', {
        domanda: domanda
	}); 
};

exports.custom = function (request, reply) {

    const domanda = [request.query];

    reply.view('index', {
        domanda: domanda
	}); 
};