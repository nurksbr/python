from pymongo import MongoClient

# MongoDB istemcisini oluştur
client = MongoClient( "mongodb+srv://ksbr1:nur1234@cluster0.u1zuhpb.mongodb.net/"
)

# Veritabanını ve koleksiyonu seç
db = client['todo_app']
collection = db['tasks']

def add_task(task):
    """Görev eklemek için fonksiyon"""
    result = collection.insert_one({'task': task, 'status': 'pending'})
    print('Yeni görev eklendi. ID:', result.inserted_id)

def get_tasks():
    """Tüm görevleri getirmek için fonksiyon"""
    tasks = collection.find({})
    for task in tasks:
        print(task)

def update_task(task_id, new_status):
    """Görevin durumunu güncellemek için fonksiyon"""
    result = collection.update_one({'_id': task_id}, {'$set': {'status': new_status}})
    if result.modified_count > 0:
        print('Görev güncellendi.')
    else:
        print('Görev bulunamadı.')

def delete_task(task_id):
    """Görevi silmek için fonksiyon"""
    result = collection.delete_one({'_id': task_id})
    if result.deleted_count > 0:
        print('Görev silindi.')
    else:
        print('Görev bulunamadı.')

# Kullanıcı arayüzü
while True:
    print("\nGörev Listesi Uygulaması\n")
    print("1. Görev Ekle")
    print("2. Tüm Görevleri Listele")
    print("3. Görev Durumunu Güncelle")
    print("4. Görev Sil")
    print("5. Çıkış")

    choice = input("Seçiminizi yapın: ")

    if choice == '1':
        task = input("Yeni görevi girin: ")
        add_task(task)
    elif choice == '2':
        get_tasks()
    elif choice == '3':
        task_id = input("Görev ID'sini girin: ")
        new_status = input("Yeni durumu girin: ")
        update_task(task_id, new_status)
    elif choice == '4':
        task_id = input("Silinecek görevin ID'sini girin: ")
        delete_task(task_id)
    elif choice == '5':
        print("Uygulamadan çıkılıyor...")
        break
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")
