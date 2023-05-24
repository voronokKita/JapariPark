# Japari Park (development)

[<img src='cover2.png' width='350'/>](cover2.png)

There will be a social network. <br>

The project has a modular architecture:

- Database (planned)
  * Sharding
- Backend on Django (planned)
  * DRF
- FriendsFrontend (WIP) <br>
  A social network "Friends", like twitter.
  * A Flask application that generates an process UI
  * An async server Gunicorn
  * NGINX proxy

The project be deployed on the Docker platform, in separate containers.

The CI-pattern is implemented on GitHub Actions. <br>
There are plans for partially or fully automated documentation.
