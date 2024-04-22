beatles_albums = Album.objects.filter(artist="Beatles")
create_nirvana = Album.objects.create(title="Nevermind", artist="Nirvana", genre="Rock")
artists_exclude_nirvana = Album.objects.exclude(artist="Nirvana")
del_smashing_pumpkins = Album.objects.filter(title="Siamese Dream").delete()
