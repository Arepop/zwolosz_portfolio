import React from 'react';
import { Container, Row, Col, Card, Image, CardDeck } from 'react-bootstrap'
import './components.css'
import 'bootstrap/dist/css/bootstrap.min.css';

export function BigBar(props) {
    if (props.side === "left") return (
        <Container fluid className='Container'>
            <Row className='h-100 Container-row'>
                <Col>
                    <Image src={props.img} className="Image"/>
                </Col>
                <Col>{props.text}</Col>
            </Row>
        </Container>
    );
    if (props.side === "rigth") return (
        <Container fluid className='Container'>
            <Row className='h-100 Container-row'>
                <Col>{props.text}</Col>
                <Col>
                    <Image src={props.img} className="Image"/>
                </Col>
            </Row>
        </Container>
    );
}

export function PreviewCard() {
return (
    <Container fulid className='CardDeck'>
        <CardDeck>
            <Row>
                <Card className='Card-background'>
                    <Card.Img variant="top" src="https://images.pexels.com/photos/459301/pexels-photo-459301.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500" />
                </Card>
                <Card className='Card-background'>
                    <Card.Img variant="top" src="https://images.pexels.com/photos/459301/pexels-photo-459301.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500" />
                </Card>
                <Card className='Card-background'>
                    <Card.Img variant="top" src="https://images.pexels.com/photos/459301/pexels-photo-459301.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500" />
                </Card>
            </Row>
            <Row>            
                <Card className='Card-background'>
                    <Card.Img variant="top" src="https://images.pexels.com/photos/459301/pexels-photo-459301.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500" />
                </Card>
                <Card className='Card-background'>
                    <Card.Img variant="top" src="https://images.pexels.com/photos/459301/pexels-photo-459301.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500" />
                </Card>
                <Card className='Card-background'>
                    <Card.Img variant="top" src="https://images.pexels.com/photos/459301/pexels-photo-459301.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500" />
                </Card>
            </Row>
        </CardDeck>
    </Container>
);
}

export function Footer() {
    return (
        <Container fluid className="Footer">
            <Row>
                <Col>All Rigths Reserved</Col>
            </Row>
            <Row>
                <Col>
                2020 Arkadiusz Popczak
                </Col>
            </Row>
        </Container>
    );
}