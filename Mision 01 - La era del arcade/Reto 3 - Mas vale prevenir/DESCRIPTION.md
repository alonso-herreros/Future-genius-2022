# **[Más vale prevenir…](https://immune.hackrocks.com/challenges/start/mas-vale-prevenir)**

| 35 Points | EASY |
|---|---|

## **Summary**
En cierto modo, a los ojos de un computador, los USB recuerdan a las jeringuillas. No es buena idea pincharte con uno si no sabes si lo ha utilizado otra persona aparte de ti, ¡pues te podrías contagiar de algo malo! Veamos cómo prevenir que se vuelvan a infectar nuestros sistemas.

## In this challenge:
- Ciberseguridad
- Python

---

Tras una extensa investigación, nuestros expertos en ciberseguridad sospechan que la causa del ciberataque fue una brecha de seguridad de lo más simplona: Uno de los empleados de VR Electronics introdujo un USB infectado con el malware en una de las computadoras de la empresa, ¡lo que dio acceso al malware a toda la red interna! No sabemos si se trató de un ataque intencionado, o si fue simplemente un error humano, pero lo que es seguro es que debemos proteger nuestros sistemas para evitar que situaciones como esta se puedan llegar a repetir en el futuro.

Como ingeniero del departamento de ciberseguridad, se te ocurre lo siguiente: Implementar un algoritmo que sólo habilite los puertos USB de las computadoras de la empresa a ciertos usuarios especiales; concretamente, a los que pertenecéis al departamento de ciberseguridad. Para ello, decides implementar un programa que se activa cuando alguien trata de conectar un dispositivo de almacenamiento externo a una computadora de la compañía. Dicho programa solicita usuario y contraseña, evalúa si dicha combinación existe en la base de datos, y si es así, habilita el puerto.

Antes de hacer el descanso para tomar el café te quedaste en la parte de evaluar si la contraseña es la correspondiente al usuario introducido, así que... ¿por dónde íbamos?

---

### **Situación inicial:**
Se proporciona un código que pide por consola un usuario y una contraseña (**[autenticar_usuario.py](autenticar_usuario.py)**). Dentro del código se encuentra la función [`authenticateUser`](autenticar_usuario.py#L1), que comprueba si el usuario introducido se encuentra en la base de datos de usuarios (almacenada en el array [`authorizedUsers`](autenticar_usuario.py#L9)).

---

### **Problema:**
La contraseña válida para cada usuario está almacenada en el array [`authorizedPasswords`](autenticar_usuario.py#L13), ocupando una posición análoga a la de su usuario correspondiente en el array [`authorizedUsers`](autenticar_usuario.py#L9). Completa el código de la función para que se compruebe si la contraseña introducida es la correspondiente al usuario introducido. Si es así, la función debe retornar `True`.

---

### **Solución:**
Sube el script **[autenticar_usuario.py](autenticar_usuario.py)** una vez lo hayas completado.