'use strict';

const Hapi = require('hapi');

const server = new Hapi.Server();
server.connection({ port: 4000 });

server.bind({
	webBaseUrl: 'http://localhost:4000'
});

server.register([
	require('inert'),
	require('vision')
	], (err) => {

	if (err) {
		throw err;
	}

	server.views({
        engines: {
        	hbs: require('handlebars')
		},
		relativeTo: __dirname,
		path: './views',
		isCached: false
	});

	server.route(require('./routes'));

	server.start(() => {

		console.log('Started server at', server.info.uri);

	});

});
