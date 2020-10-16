from xmlrpc import client

url = 'https://jsz-odoo-odoo-training-js-tech-training-jsz-1578102.dev.odoo.com'
db = 'jsz-odoo-odoo-training-js-tech-training-jsz-1578102'
username = 'admin'
password = 'admin'

common = client.ServerProxy('{}/xmlrpc/2/common'.format(url))
print(common.version())

uid = common.authenticate(db, username, password, {})
print(uid)

models = client.ServerProxy('{}/xmlrpc/2/object'.format(url))

model_access = models.execute_kw(db, uid, password,
                                 'library.loan', 'check_access_rights',
                                 ['write'], {'raise_exception': False})

print(model_access)

books = models.execute_kw(db, uid, password,
                          'library.book', 'search_read',
                          [[['page_length', '<', 300]]])

print(books)

book = models.execute_kw(db, uid, password,
                         'library.book', 'search',
                         [[['name', '=', "The Hitchhiker's Guide to the Galaxy"]]])

print(book)

loan_fields = models.execute_kw(db, uid, password,
                                'library.loan', 'fields_get',
                                [], {'attributes': ['string', 'type', 'required']})

print(loan_fields)

new_loan = models.execute_kw(db, uid, password,
                             'library.loan', 'create',
                             [
                                 {
                                     'active': False,
                                     'name': 'Another Loan',
                                 }
                             ])

print(new_loan)