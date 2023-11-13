import matplotlib.pyplot as plt

# Datos de cantidad demandada
precio = [40, 50, 60, 70, 80, 90, 100]  
cantidad_demandada = [170, 160, 150, 140, 130, 120, 110]

# Datos de cantidad ofrecida
cantidad_ofrecida = [120, 130, 140, 150, 160, 170, 180]

# Graficar oferta y demanda
fig, ax = plt.subplots()
ax.plot(cantidad_demandada, precio, label='Demanda') 
ax.plot(cantidad_ofrecida, precio, label='Oferta')

# Etiquetas
ax.set_xlabel('Cantidad')
ax.set_ylabel('Precio (Lempiras)')
ax.set_title('Mercado de almuerzos')
ax.legend()

# Mostrar equilibrio 
plt.plot(150, 70, 'ro')
plt.text(155, 75, 'Equilibrio', fontsize=12) 

plt.show()