
document.getElementById('inputfile')
            .addEventListener('change', function () {

                let fr = new FileReader();
                fr.onload = function () {
                    

                        let assign_count = 0; //assign node

                        let select_count = 0; //start node
                        let end_count = 0; //end node

                        let click = false;
                        let index_str; //convert index to string

                        let display_words_list = [];
                        let found_words_list = [];
                        let start_pos_list = [];
                        let end_pos_list = [];

                        document.getElementById('wordfile')
                            .addEventListener('change', function () {

                                fr = new FileReader();
                                fr.onload = function () {
                                    

                                        
                                        const fr_string = fr.result.slice(0, fr.result.length - 1)
                                
                                        let wordArray = fr_string.split(";");
                                        

                                        

                                        for (let wordindex = 0; wordindex < wordArray.length; wordindex ++) {
                                            temp_string = wordArray.at(wordindex).split(",");
                                            display_words_list.push(temp_string[0])
                                            start_pos_list.push(Number(temp_string[1]))
                                            end_pos_list.push(Number(temp_string[2]))
                                        }

                                        
                                        
                                        for (let display_word of display_words_list) {
                                            if (display_word != undefined) {
                                                document.getElementById("wordlist").textContent += display_word + "\r\n";
                                            } else {
                                                document.getElementById("wordlist").textContent += display_word;
                                            }
                                            
                                        }
                                    }

                                    fr.readAsText(this.files[0]);
                                })
                            
                        for (let node of document.querySelectorAll("td")) {

                            node.onclick = function() {
                                
                                if (node.className != "selected_end" && click == true) {
                                    click = false;
                                    
                                    for (let index = 0; index < 400; index++) {
                                        switch(true) {
                                            case (index < 10):
                                                index_str = "00" + String(index);
                                                break;
                                            case (index < 100):
                                                index_str = "0" + String(index);
                                                break;
                                            default:
                                                index_str = String(index);
                                        }

                                        if (document.getElementById(index_str).className == "selected_end" || document.getElementById(index_str).className == "selected_start") {
                                            document.getElementById(index_str).className = index_str
                                        }
                                    }
                                    
                                } else if (node.className == "selected_end" && click == true) {
                                    let found = false; // detects when a word is found
                                    let finish_game = true; // detects when all words are found
                                    found_list = [];

                                    end_count = Number(node.id)

                                    for (let j = 0; j < display_words_list.length; j++) {
                                        if (select_count == start_pos_list[j] && end_count == end_pos_list[j]) {
                                            found = true;
                                            found_words_list.push(display_words_list[j])
                                            delete display_words_list[j];

                                            document.getElementById("wordlist").textContent = "";
                                            document.getElementById("wordsfound").textContent = "";

                                            for (let display_word of display_words_list) {
                                                if (display_word != undefined && display_word != display_words_list[-1]) {
                                                    document.getElementById("wordlist").textContent += display_word + "\r\n";
                                                    finish_game = false;
                                                }
                                            }
    
                                            for (let found_word of found_words_list) {
                                                if (found_word != undefined) {
                                                    document.getElementById("wordsfound").textContent += found_word + "\r\n"
                                                }
                                            }

                                            break;
                                        }
                                    }
                                    
                                    if (!found) {
                                        end_count = Number(node.id)
                                        window.alert(`not a valid word!`)
                                    } else if (finish_game) {
                                        document.getElementById("wordlist").textContent = `All words have been found, thank you for playing!`
                                    }

                                


                                } else {
                                    click = true;
                                    select_count = Number(node.className)
                                    node.className = "selected_start";
                                    let repeated_1 = false;
                                    let start_1 = false;
                                    let repeated_2 = false;
                                    let start_2 = false;

                                    for (let i = 0; i < 400; i++) {
                                        
                                        let element;

                                        if (select_count - (select_count % 20) <= i && i < 20 + select_count - (select_count % 20) && i != select_count) { //horizontal

                                            switch(true) {
                                                case (i < 10):
                                                    index_str = "00" + String(i);
                                                    break;
                                                case (i < 100):
                                                    index_str = "0" + String(i);
                                                    break;
                                                default:
                                                    index_str = String(i);
                                            }

                                            element = document.getElementById(index_str);
                                            element.className = "selected_end";                                            
                                            
                                        } else if ((select_count - i) % 20 == 0 && i != select_count) { //vertical

                                            switch(true) {
                                                case (i < 10):
                                                    index_str = "00" + String(i);
                                                    break;
                                                case (i < 100):
                                                    index_str = "0" + String(i);
                                                    break;
                                                default:
                                                    index_str = String(i);
                                            }

                                            element = document.getElementById(index_str);
                                            element.className = "selected_end";                                  
                                            

                                        } else if ((select_count - i) % 21 == 0 && i != select_count && !repeated_1 && select_count != 19 && select_count != 380) { // \ diagonal
                                            if (i % 20 == 0) {
                                                start_1 = true;
                                            }
                                    
                                            if (select_count % 21 == 0) {
                                                switch(true) {
                                                    case (i < 10):
                                                        index_str = "00" + String(i);
                                                        break;
                                                    case (i < 100):
                                                        index_str = "0" + String(i);
                                                        break;
                                                    default:
                                                        index_str = String(i);
                                                }
                                                element = document.getElementById(index_str);
                                                element.className = "selected_end";            

                                            } else if (select_count % 20 - Math.floor(select_count / 20) > 0) {
                                                switch(true) {
                                                    case (i < 10):
                                                        index_str = "00" + String(i);
                                                        break;
                                                    case (i < 100):
                                                        index_str = "0" + String(i);
                                                        break;
                                                    default:
                                                        index_str = String(i);
                                                }
                                                element = document.getElementById(index_str);
                                                element.className = "selected_end";
                                                if (i % 20 == 19) {
                                                    repeated_1 = true;
                                                }

                                            } else if (start_1) {
                                                switch(true) {
                                                    case (i < 10):
                                                        index_str = "00" + String(i);
                                                        break;
                                                    case (i < 100):
                                                        index_str = "0" + String(i);
                                                        break;
                                                    default:
                                                        index_str = String(i);
                                                }
                                                element = document.getElementById(index_str);
                                                element.className = "selected_end";
                                                if (Math.floor(i / 20) == 19) {
                                                    repeated_1 = true;
                                                }
                                            }

                                            if (i + 21 == select_count && select_count %  20 == 19 && !start_1) {
                                                repeated_1 = true
                                            }

                                        } else if ((select_count - i) % 19 == 0 && i != select_count && !repeated_2 && i != 0 && i != 399 && select_count != 0 && select_count != 399) { // / diagonal
                                            if (i % 20 == 19) {
                                                start_2 = true;
                                            }
                                    
                                            if (select_count % 19 == 0) {
                                                switch(true) {
                                                    case (i < 10):
                                                        index_str = "00" + String(i);
                                                        break;
                                                    case (i < 100):
                                                        index_str = "0" + String(i);
                                                        break;
                                                    default:
                                                        index_str = String(i);
                                                }
                                                element = document.getElementById(index_str);
                                                element.className = "selected_end";            

                                            } else if (select_count % 20 + Math.floor(select_count / 20) < 19) {
                                                switch(true) {
                                                    case (i < 10):
                                                        index_str = "00" + String(i);
                                                        break;
                                                    case (i < 100):
                                                        index_str = "0" + String(i);
                                                        break;
                                                    default:
                                                        index_str = String(i);
                                                }
                                                element = document.getElementById(index_str);
                                                element.className = "selected_end";
                                                if (i % 20 == 0) {
                                                    repeated_2 = true;
                                                }

                                            } else if (start_2) {
                                                switch(true) {
                                                    case (i < 10):
                                                        index_str = "00" + String(i);
                                                        break;
                                                    case (i < 100):
                                                        index_str = "0" + String(i);
                                                        break;
                                                    default:
                                                        index_str = String(i);
                                                }
                                                element = document.getElementById(index_str);
                                                element.className = "selected_end";
                                                if (i % 20 == 0) {
                                                    repeated_2 = true;
                                                }
                                            }     
                                            
                                            if (i + 19 == select_count && select_count %  20 == 0 && !start_2) {
                                                repeated_2 = true;
                                            }

                                        } else if (i == select_count) {
                                            start_1 = true;
                                            start_2 = true;
                                        }
                                    }
                                }
                                
                            }


                            node.textContent = fr.result.charAt(assign_count)

                            switch(true) {
                                case (assign_count < 10):
                                    node.className = "00" + String(assign_count);
                                    node.id = "00" + String(assign_count);
                                    break;
                                case (assign_count < 100):
                                    node.className = "0" + String(assign_count);
                                    node.id = "0" + String(assign_count);
                                    break;
                                default:
                                    node.className = String(assign_count)
                                    node.id = String(assign_count)

                            }
                            

                            
                            
                            assign_count += 1;
                        }
                    
                }

                fr.readAsText(this.files[0]);
            })
        
            


            
