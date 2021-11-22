class User:
	def __init__(self): ## konstruktor
		self.nama = "Galih Subandono"
		self.jobtitle = "President"
		self.deskripsi = "Saya developer dah itu aja saya developer dah itu aja saya developer dah itu aja saya developer dah itu aja saya developer dah itu aja saya developer dah itu aja saya developer dah itu aja saya developer dah itu aja saya developer dah itu aja saya developer dah itu aja saya developer dah itu aja saya developer dah itu aja saya developer dah itu aja saya developer dah itu aja "
		self.foto = "/profile/galih.jpg"

	def get(self): ## method untuk mengambil nama
		data = {
			'nama':self.nama,
			'jobtitle':self.jobtitle,
			'deskripsi':self.deskripsi,
			'foto':self.foto
		}
		return data
