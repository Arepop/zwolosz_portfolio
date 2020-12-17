import { Switch, Route } from 'react-router-dom';
import { useQuery } from '@apollo/react-hooks';
import { TILE_LIST_QUERY } from "./query"
import './App.css';
import { BigBar, PreviewCard, Footer } from "./components"
import { Spinner, Button} from 'react-bootstrap'
import './components.css'


function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Switch>
          <Route exact path="/" component={MainPage}></Route>
        </Switch>
      </header>
    </div>
  );
}

export default App;

const MainPage = (props) => {
  const { loading, error, data } = useQuery(TILE_LIST_QUERY);
  if (loading) return (<Spinner animation="border" role="status">
                      </Spinner>);
  if (error) return <div>Unexpected Error: {error.message}</div>

  return(
    <div style={{width: "100vw"}}>
          <Button className="btn button circular btn-dark">=</Button>
          <BigBar img={data.allTiles.edges[0].node.fileName} text={data.allTiles.edges[0].node.name} side={'left'}></BigBar>
          <BigBar img={data.allTiles.edges[0].node.fileName} text={data.allTiles.edges[0].node.name} side={'rigth'}></BigBar>
          <PreviewCard></PreviewCard>
          <Footer></Footer>
    </div>
  );
}
