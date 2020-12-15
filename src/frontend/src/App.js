import { Switch, Route } from 'react-router-dom';
import { useQuery } from '@apollo/react-hooks';
import { TILE_LIST_QUERY } from "./query"

import './App.css';


const MainPage = (props) => {
  const { loading, error, data } = useQuery(TILE_LIST_QUERY);
  if (loading) return <div>Loading</div>
  if (error) return <div>Unexpected Error: {error.message}</div>

  return(
    <div>
        <div>
            <p>{data.allTiles.edges[0].node.name}</p>
        </div>
    </div>
  )
}

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
