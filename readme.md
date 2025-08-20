## API Cadastro
API feita em Django Rest Framework para cadastro, consulta e gerenciamento de dados imobiliários urbanos, incluindo bairros, logradouros, edificações, lotes, pessoas, quadras, setores e zoneamento. Projetada para facilitar integrações e operações geoespaciais em sistemas municipais ou corporativos.

O objetivo deste projeto foi praticar e aprimorar meus conhecimentos.

---

### Endpoints
- Lote
  - CRUD completo para lote
  - `GET /lote/{id}/edificacoes/`: Lista as edificações de um lote específico
  - `GET /lote/{id}/proprietarios/`: Lista todos os proprietários vinculados ao lote específico
  - `POST /lote/intersects/`: Lista os zoneamentos a partir de uma intersecção com uma geometria de lote
- Imobiliário
  - CRUD completo para imobiliario
  - `GET /imobiliario/proximos/?raio=20&point=POINT (-48.8 -27.0)`: Lista imobiliarios dentro de um raio a partir de uma localização
- Quadra
  - CRUD completo para quadra
  - `GET /quadra/area-construida/`: Lista o total de área construída por quadra
- Bairro
  - CRUD completo para bairro
  - `GET /bairro/{id}/edificacoes/`: Lista todas as edificações de um bairro específico
- Zoneamento
  - CRUD completo para zoneamento
  - `GET /zoneamento/utilizacao-terreno/`: Para cada zoneamento, retorna a quantidade de lotes agrupado pelo campo utilizacao_terreno
- Edificação
  - CRUD completo para edificacao
- Pessoa
  - CRUD completo para pessoa
- Logradouro
  - CRUD completo para logradouro
- Setor
  - CRUD completo para setor