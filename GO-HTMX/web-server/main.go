package main

import (
	"fmt"
	"html/template"
	"log"
	"net/http"
)

type Film struct {
	Title string
	Director string

}

func main() {
	fmt.Println("Hello world")

	// writingh to the web server
	h1 := func(w http.ResponseWriter, r *http.Request) {
		
		// to send a direct message
		// io.WriteString(w, "Hello world/n")
		// io.WriteString(w, r.Method)

		// to send a template
		tmpl := template.Must(template.ParseFiles("index.html"))
		films := map[string][]Film{
			"Films": {
				{Title: "The Godfather", Director: "Francis Ford Coppola"},
				{Title: "Blade Runner", Director: "Ridley Scott"},
				{Title: "The Thing", Director: "John Carpenter"},
			},
		}
		tmpl.Execute(w, films)
	}

	// handling requests
	http.HandleFunc("/", h1)

	log.Fatal(http.ListenAndServe(":8080", nil))
}
