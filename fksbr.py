from pymongo import MongoClient

# MongoDB bağlantı bilgileri
uri = "mongodb+srv://ksbr1:nur1234@cluster0.u1zuhpb.mongodb.net/"

  # MongoDB URI
database_name = "mydatabase"  # Veritabanı adı
collection_name = "users"  # Koleksiyon adı

# Kullanıcı bilgileri
user_data = {
    "username": "example_user",
    "email": "user@example.com",
    "password": "password123",
    # İhtiyaca göre diğer alanları da ekleyebilirsiniz
}

# MongoDB istemcisini oluştur
client = MongoClient(uri)

# Veritabanını ve koleksiyonu al
database = client[database_name]
collection = database[collection_name]

# Kullanıcıyı koleksiyona ekle
result = collection.insert_one(user_data)

# Sonucu kontrol et
if result.inserted_id:
    print("Kullanıcı başarıyla eklendi. Kullanıcı ID:", result.inserted_id)
else:
    print("Kullanıcı eklenirken bir hata oluştu.")
