import socketio

# Нет авторизации и персональных данных – нет проблем с безопасностью!
sio = socketio.Server(cors_allowed_origins="*", origins="*")

# Сервим статику (хотя пока она нам и не нужна)
# app = socketio.WSGIApp(sio, static_files={
#         '/': {'content_type': 'text/html', 'filename': 'static/index.html'},
#         '/main.js': {'content_type': 'text/javascript', 'filename': 'static/scripts/main.js'}
#     },
# )
