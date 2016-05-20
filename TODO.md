# TODO

## REST api

- [x] routing for api calls
  - [x] should use falcon hooks
  - [ ] forum
  - [x] pages
  - [ ] dashboard
    - [ ] should modify configuration
  - [ ] blog
- [ ] socketio, haproxy
- [x] gunicorn custom application
  - [x] gunicorn worker class
  - [x] make gunicorn import workers conditionally
- [ ] authentication
  - [ ] need conditional authentication for certain routes
  - [ ] google oauth playground
  - [ ] support multiple oauth services (goog, fb)

### Done
- [x] create test script
- [x] refactor api to falcon from flask
