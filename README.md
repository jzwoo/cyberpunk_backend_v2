# cyberpunk_backend_v2

.env
```
MONGO_USERNAME=cyberpunk
MONGO_PASSWORD=password
MONGO_DB_URI=mongodb://localhost:27017/cyberpunk-db

JWT_SECRET=your_secret_key1
REFRESH_TOKEN_SECRET=your_secret_key2

GOOGLE_CLIENT_ID=<GOOGLE CLIENT ID>

KONG_DATABASE=postgres
```

.gateway/output/POSTGRES_PASSWORD
```
kong
```
Start the application with kong as db mode
```
docker compose --profile database up -d
```
Make sure to sync the database with kong
```
# deck is a dependency
# download deck_<latest version>_amd64.deb from https://github.com/Kong/deck/releases
# sudo dpkg -i deck_v1.47.0_amd64.deb 
# sudo apt-get install -f
# check if installed: deck version

# 8001 is the admin endpoint
deck sync --kong-addr http://localhost:8001 --state kong.yaml
```