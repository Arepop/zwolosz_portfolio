import { Switch, Route } from 'react-router-dom';
import { useQuery } from '@apollo/react-hooks';
import { TILE_LIST_QUERY } from "./query"
import React from 'react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Container, Col, Row } from 'react-bootstrap'


const MainPage = (props) => {
  const { loading, error, data } = useQuery(TILE_LIST_QUERY);
  if (loading) return <div>Loading</div>
  if (error) return <div>Unexpected Error: {error.message}</div>

  return(
            <Grid>Grid</Grid>
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


function Grid() {
  return (
<Container fluid style={{height: "100vw"}}>
  <Row style={{backgroundColor: "gray", height: "100wv"}}>
    <Col>Tutaj będzie znajdować się obrazek który Zosia zrobi</Col>
    <Col>A tutaj będzie tekst</Col>
  </Row>
  <Row style={{backgroundColor: "darkgray", height: "100vw"}}>
    <Col>Tutaj będzie znajdować się obrazek który Zosia zrobi</Col>
    <Col>A tutaj będzie tekst</Col>
  </Row>
</Container>
  )
}