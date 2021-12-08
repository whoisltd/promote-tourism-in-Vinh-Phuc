window.onscroll = () => {
  if (window.scrollY > 0) {
    document
      .querySelector(".placePage-header_navbar")
      .classList.add("active--navbar");
  } else {
    document
      .querySelector(".placePage-header_navbar")
      .classList.remove("active--navbar");
  }
};
