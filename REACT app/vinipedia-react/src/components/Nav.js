import styled from "styled-components";

export default function Nav() {
  return (
    <StyledNav>
      <div class="menu">
        <a class="logo" href="{% url 'homepage' %}">
          <img src="/media/icons/Winecense_logo.png" />
        </a>
        <a class="menu-page" href="{% url 'wine:wine_list' %}">
          All Wines
        </a>
      </div>
    </StyledNav>
  );
}

const StyledNav = styled.nav`
  body {
    font-family: "Montserrat", sans-serif;
    width: 100%;
    min-height: 100vh;
    margin: 0;
  }

  a {
    color: #58595b;
    text-decoration: none;
    transition: 0.3s;
  }

  a:hover {
    text-shadow: 0 0.1em 0.2em #ba3f1d7c;
    transition: 0.15s;
  }

  .menu {
    height: 100%;
    width: 50%;
    display: flex;
    align-items: center;
    padding: 0 3.125vw;
  }

  .menu img {
    height: 100%;
  }

  .logo {
    height: 100%;
    max-height: 50%;
  }

  .menu-page {
    margin-left: 3.125vw;
  }

  nav {
    height: 6.25vh;
    background-color: white;
    border-bottom: solid #e6e7e8 1px;
    position: fixed;
    width: 100%;
    top: 0;
    z-index: 50;
    display: flex;
  }
`;
