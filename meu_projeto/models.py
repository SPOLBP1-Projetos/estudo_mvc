class UsuarioModel:
#Simula um 'banco de dados' em memória e a lógica de negócio. Em um projeto real, aqui estariam as chamadas ao SQLAIchemy, etc.

# Dados em memória para simplificar 
    _usuarios = [
    {'id': 1, 'nome': 'Ana Silva', 'email': 'ana@email.com'},
    {'id': 2, 'nome': 'Bruno Costa', 'email': 'bruno@email.com'}
]
    _next_id = 3


    def get_todos(self):
        """Retorna todos os usuários."""
        return self._usuarios

    def get_um(self,user_id):
        """Retorna um único usuário pelo ID."""
        for user in self._usuarios:
            if user['id'] == user_id:
                return user
            return None

    def salvar(self, nome, email):
        """Salva um novo usuário e retorna ele."""

        novo_usuario = {'id': self._next_id, 'nome': nome, 'email': email}
        self._usuarios.append(novo_usuario)
        self._next_id += 1
        return novo_usuario
    
