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

exports.thanks = function (request, reply) {

    const risposta = [request.query];

    reply.view('answer', {
        risposta: risposta
    });
  
};

exports.err = function (request, reply) {

    reply.view('error');
  
};

exports.report = function (request, reply) {

    const sql = 'INSERT INTO risposte (istante, domanda, voto) VALUES (?,?,?)';

    this.db.run(sql, 
    [
        request.payload.istante,
        request.payload.domanda,
        request.payload.voto
    ],
    (err) => {

        if (err) {
            throw err;
        }

        reply({ status: 'ok'});

    });

    
};