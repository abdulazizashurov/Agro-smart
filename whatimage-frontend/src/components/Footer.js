import React from 'react'
import {Container, Row,Col} from 'react-bootstrap'

function Footer() {
    return (
        <footer>
            <Container>
                <Row>
                    <Col className="py-3 text-center">Copyright &copy; <a href="https://t.me/su11360">Agro-Smart</a></Col>
                </Row>
            </Container>
        </footer>
    )
}

export default Footer