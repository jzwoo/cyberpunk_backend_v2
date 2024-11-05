db = db.getSiblingDB("cyberpunk-db");

db.createUser({
    user: process.env.MONGO_USERNAME,
    pwd: process.env.MONGO_PASSWORD,
    roles: [{role: "readWrite", db: "cyberpunk-db"}],
});

// alternatively, "db.createCollection" creates a new collection without adding data
// db.createCollection('asset')

// db.createCollection('products')
db.createCollection('carts')
db.products.insert([
    {
        id: "16524425-56f3-41d3-a0f7-7c52b66030d1",
        name: "MiG Turbo",
        description: "Product 1 description",
        image: {
            url: "/store/drones/drone1.png",
            aspectRatio: 0.1
        },
        price: 890,
        quantity: 2
    },
    {
        id: "16524425-56f3-41d3-a0f7-7c52b66030d2",
        name: "Mini-1000",
        description: "Product 2 description",
        image: {
            url: "/store/drones/drone2.png",
            aspectRatio: 0.1
        },
        price: 680,
        quantity: 2
    },
    {
        id: "16524425-56f3-41d3-a0f7-7c52b66030d3",
        name: "Mini Plus",
        description: "Product 3 description",
        image: {
            url: "/store/drones/drone3.png",
            aspectRatio: 0.1
        },
        price: 800,
        quantity: 2
    },
    {
        id: "16524425-56f3-41d3-a0f7-7c52b66030d4",
        name: "DJI INspire 3",
        description: "Product 4 description",
        image: {
            url: "/store/drones/drone4.png",
            aspectRatio: 0.1
        },
        price: 920,
        quantity: 2
    },
    {
        id: "16524425-56f3-41d3-a0f7-7c52b66030d5",
        name: "DJI Mavic Pro Premium",
        description: "Product 5 description",
        image: {
            url: "/store/drones/drone5.png",
            aspectRatio: 0.1
        },
        price: 820,
        quantity: 2
    },
    {
        id: "16524425-56f3-41d3-a0f7-7c52b66030d6",
        name: "DJI Avata",
        description: "Product 6 description",
        image: {
            url: "/store/drones/drone6.png",
            aspectRatio: 0.1
        },
        price: 719,
        quantity: 2
    },
    {
        id: "16524425-56f3-41d3-a0f7-7c52b66030d7",
        name: "DJI Mini 2",
        description: "Product 7 description",
        image: {
            url: "/store/drones/drone7.png",
            aspectRatio: 0.1
        },
        price: 500,
        quantity: 2
    },
    {
        id: "16524425-56f3-41d3-a0f7-7c52b66030d8",
        name: "DJI Agras T40",
        description: "Product 8 description",
        image: {
            url: "/store/drones/drone8.png",
            aspectRatio: 0.1
        },
        price: 26519,
        quantity: 2
    },
    {
        id: "16524425-56f3-41d3-a0f7-7c52b66030d9",
        name: "DJI Mavic 3M",
        description: "Product 9 description",
        image: {
            url: "/store/drones/drone9.png",
            aspectRatio: 0.1
        },
        price: 1000,
        quantity: 2
    },
    {
        id: "16524425-56f3-41d3-a0f7-7c52b6603010",
        name: "DJI Drone 10",
        description: "Product 10 description",
        image: {
            url: "/store/drones/drone10.png",
            aspectRatio: 0.1
        },
        price: 2000,
        quantity: 2
    },
    {
        id: "16524425-56f3-41d3-a0f7-7c52b6603011",
        name: "DJI Drone 11",
        description: "Product 11 description",
        image: {
            url: "/store/drones/drone11.png",
            aspectRatio: 0.1
        },
        price: 4500,
        quantity: 2
    },
    {
        id: "16524425-56f3-41d3-a0f7-7c52b6603012",
        name: "DJI Drone 12",
        description: "Product 12 description",
        image: {
            url: "/store/drones/drone12.png",
            aspectRatio: 0.1
        },
        price: 5000,
        quantity: 2
    },
    {
        id: "16524425-56f3-41d3-a0f7-7c52b6603013",
        name: "DJI Drone 13",
        description: "Product 13 description",
        image: {
            url: "/store/drones/drone13.png",
            aspectRatio: 0.1
        },
        price: 10000,
        quantity: 2
    }
])