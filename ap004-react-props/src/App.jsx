import Cartao from "./Cartao"
import Pedido from "./Pedido"
export default () => {
  return (
    <div className="container border">
      <div className="row">

        <div className="col-12">
          {/* i.fa-solid.fa-hippo */}
          <i className="fa-solid fa-hippo fa-2x"></i>
        </div>

      </div>
      <div className="row">
        <div className="col-sm-12 col-md-6 col-xl-3">
            <Cartao
                cabecalho="22/02/2026">
                <Pedido
                    icone="camera"
                    titulo="Câmera"
                    descricao="Uma câmera 4K"/>
            </Cartao>  
        </div>
        <div className="col-sm-12 col-md-6 col-xl-3">
          <Cartao
                cabecalho="15/02/2026">
                <Pedido
                    icone="book"
                    titulo="Livro"
                    descricao="Concrete Maths"/>
            </Cartao>  
        </div>
        <div className="col-sm-12 col-md-6 col-xl-3">
          <Pedido />
        </div>
        <div className="col-sm-12 col-md-6 col-xl-3">
          <Pedido />
        </div>
      </div>
    </div>
  )
}