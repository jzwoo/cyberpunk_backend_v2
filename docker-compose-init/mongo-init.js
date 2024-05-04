db = db.getSiblingDB("cyberpunk-db");

db.createUser({
    user: process.env.MONGO_USERNAME,
    pwd: process.env.MONGO_PASSWORD,
    roles: [{role: "readWrite", db: "cyberpunk-db"}],
});

// alternatively, "db.createCollection" creates a new collection without adding data
// db.createCollection('asset')

db.products.insert([
    {
        uuid: "16524425-56f3-41d3-a0f7-7c52b66030d6",
        name: "product 1",
        description: "Product 1 description",
        image: {
            url: "",
            aspectRatio: 0.1
        },
        price: 1,
        quantity: 2
    },
    {
        uuid: "16524425-56f3-41d3-a0f7-7c52b66030d6",
        name: "product 2",
        description: "Product 2 description",
        image: {
            url: "",
            aspectRatio: 0.1
        },
        price: 1,
        quantity: 2
    },
    {
        uuid: "16524425-56f3-41d3-a0f7-7c52b66030d6",
        name: "product 3",
        description: "Product 3 description",
        image: {
            url: "",
            aspectRatio: 0.1
        },
        price: 1,
        quantity: 2
    },
    {
        uuid: "16524425-56f3-41d3-a0f7-7c52b66030d6",
        name: "product 4",
        description: "Product 4 description",
        image: {
            url: "",
            aspectRatio: 0.1
        },
        price: 1,
        quantity: 2
    },
    {
        uuid: "16524425-56f3-41d3-a0f7-7c52b66030d6",
        name: "product 5",
        description: "Product 5 description",
        image: {
            url: "",
            aspectRatio: 0.1
        },
        price: 1,
        quantity: 2
    }
])

// db.createCollection('products')
db.createCollection('users')
