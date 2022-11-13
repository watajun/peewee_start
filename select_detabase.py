from database import Thread

threads = Thread.select()
print(threads[0].name)
print(threads[3].name)

Thrads = Thread.select(name="Keisuke01", title="Title01", body="Body01")
print(threads.name)
