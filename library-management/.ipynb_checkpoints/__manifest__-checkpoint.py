# -*- coding: utf-8 -*-

{
    'name': 'Library Management',
    
    'version': '1.0',
    
    'description': """
        Library Management App
        Manage your library with ease!
        - Organize Books
        - Check on Rentals
        - Manage customers and anything they have checked out
    """,
    
    'author': 'Johnny Sanchez',
    
    'depends': ['base'],
    
    'data': [
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'views/library_management_menuitems.xml',
        'views/manager_views.xml',
        'views/book_views.xml',
        'views/patron_views.xml',
        'views/loan_views.xml'
    ],
    
    'demo': [
        'demo/manager_demo.xml',
        'demo/book_demo.xml',
        'demo/patron_demo.xml'
    ]
}