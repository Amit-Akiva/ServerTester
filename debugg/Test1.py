from infrastructure import rest_api_routes

host = rest_api_routes.host

user_in = rest_api_routes.get_user('Amit')
# print(f'{host}')

print(f'{user_in}')
