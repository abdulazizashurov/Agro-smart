import React from 'react'
import {Container,Navbar,Nav} from 'react-bootstrap'


function Header() {

    return (
        <header>
            <Navbar bg="dark" variant="dark" expand="lg" collapseOnSelect>
                <Container>
                        <Navbar.Brand href="/">Agro-Smart</Navbar.Brand>
                    <Navbar.Toggle aria-controls="basic-navbar-nav" />
                    <Navbar.Collapse id="basic-navbar-nav">
                        <Nav className="mr-auto">
                        <Nav.Link href="https://t.me/agro_smart_hackaton_bot"><i className="fas fa-source"></i>Telegram bot</Nav.Link>
                        </Nav>
                    </Navbar.Collapse>
                </Container>
                </Navbar>
        </header>
    )
}

export default Header
