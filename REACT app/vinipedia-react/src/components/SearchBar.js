import search from "../media/icons/search.png";

export default function SearchBar() {
    return (
 
 <form class="search_box" method="GET" action="" accept-charset="UTF-8">
    <input class="search-button" type="image" src={search} value="Search">
  </form>

  );
}