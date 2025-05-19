{
    'name':"Automobile",
    'version':"17.0.1.0.0",
    'summary':'Module for Managing Automobile Industry Operations',
    'description':'This Module Helps to maintain truck sales, maintainence,sales & inventory management',
    'author':'Niket',
    'category':"Automobile",
    'depends': ['base','mail'],
    'data':[
        'security/ir.model.access.csv',
        'views/cars_view.xml',
        'views/cars_readonly_view.xml',   
        'views/parts_view.xml',
        'wizard/vehicle_service_wizard_view.xml',
        'wizard/automobile_menus.xml',
    ],
    'installable':True,
    'license':"LGPL-3",
    'application': True
}
