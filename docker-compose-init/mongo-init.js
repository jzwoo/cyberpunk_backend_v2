db = db.getSiblingDB("cyberpunk-db");

db.createUser({
    user: process.env.MONGO_USERNAME,
    pwd: process.env.MONGO_PASSWORD,
    roles: [{role: "readWrite", db: "cyberpunk-db"}],
});

// 1. creates a collection called "asset"
// 2. inserts data
// db.asset.insert([
//     {
//         uuid: "16524425-56f3-41d3-a0f7-7c52b66030d6",
//         network_zone: "internal",
//         authentication: "single-factor",
//         need_firewall_clearance: false,
//         need_privileged_access: true,
//         recovery_time_objective: "critical",
//         data_sensitivity_level: "highly_sensitive",
//     },
//     {
//         uuid: "ae0e8143-7fc3-496e-a3a3-3d46a41a6e06",
//         network_zone: "secure-internal",
//         authentication: "multi-factor",
//         need_firewall_clearance: true,
//         need_privileged_access: true,
//         recovery_time_objective: "low",
//         data_sensitivity_level: "public",
//     }
// ]);

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
    }
])

// db.createCollection('products')
db.createCollection('users')
