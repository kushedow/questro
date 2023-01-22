import socketio

# Нет авторизации и персональных данных – нет проблем с безопасностью!
sio = socketio.Server(cors_allowed_origins="*", origins="*")

# Сервим статику (хотя пока она нам и не нужна)
app = socketio.WSGIApp(sio, static_files={

        '/': {'content_type': 'text/html', 'filename': 'questro_frontend/dist/index.html'},

        '/assets/index-8806e07e.js': {'content_type': 'text/javascript', 'filename': 'questro_frontend/dist/assets/index-8806e07e.js'},

        '/assets/index-6516db60.css': {'content_type': 'text/javascript', 'filename': 'questro_frontend/dist/assets/index-6516db60.css'},

    },
)

