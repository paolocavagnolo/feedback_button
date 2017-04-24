'use strict';

const Pages = require('./handlers/pages');
const Assets = require('./handlers/assets');

module.exports = [{

    method: 'GET',
    path: '/',
    handler: Pages.home

    }, {

    method: 'GET',
    path: '/domanda/',
    handler: Pages.custom

    }, {

    method: 'GET',
    path: '/risposta/',
    handler: Pages.thanks

    }, {

    method: 'GET',
    path: '/errore/',
    handler: Pages.err

    }, {

    method: 'POST',
    path: '/risposta/', 
    handler: Pages.report

    }, {

    method: 'GET',
    path: '/{param*}',
    handler: Assets.servePublicDirectory



}];