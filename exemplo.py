class ContextoSimples:

  def __enter__(self):
    print("Inciar conexão")
    return self
  
  def __exit__(self, exc_type, exc_value,exc_traceback):
    print("Encerrar conexão")

with ContextoSimples() as contexto:
  print("Execução dentro do DB")