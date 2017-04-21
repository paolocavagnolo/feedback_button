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
    path: '/{param*}',
    handler: Assets.servePublicDirectory



}];