from pymongo import MongoClient

# MongoDB bağlantı bilgileri
uri = "mongodb+srv://ksbr1:nur1234@cluster0.u1zuhpb.mongodb.net/"
  # MongoDB URI
database_name = "mydatabase"  # Veritabanı adı
collection_name = "messages"  # Koleksiyon adı

# Kaydedilecek metin
message_text = input("Kaydetmek istediğiniz metni girin: ")

# MongoDB istemcisini oluştur
client = MongoClient(uri)

# Veritabanını ve koleksiyonu al
database = client[database_name]
collection = database[collection_name]

# Metni koleksiyona ekle
message_data = {"message": message_text}
result = collection.insert_one(message_data)

# Sonucu kontrol et
if result.inserted_id:
    print("Mesaj başarıyla kaydedildi. Mesaj ID:", result.inserted_id)
else:
    print("Mesaj kaydedilirken bir hata oluştu.")
