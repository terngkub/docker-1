(* main.ml *)

let ft_string_all (f : char -> bool) (x : string) : bool =
  let rec ofs (y : int) =
    if y = String.length x then true
    else (
      if f (String.get x y) = true then ofs (y + 1)
      else false
    )
  in ofs 0

let is_digit c = c >= '0' && c <= '9'


let parse board =
  let rec loop () =
    let input = read_line () in
    let splited = String.split_on_char ' ' input in
    match splited with
    | grid_str :: piece_str :: [] ->
       (* Dummy error handling *)
       if String.length grid_str > 1 || String.length piece_str > 1
          || ft_string_all is_digit grid_str != true
          || ft_string_all is_digit piece_str != true
       then
         ( print_endline "Incorrect format"; loop () )
       else
         let grid_num = int_of_string grid_str in
         let piece_num = int_of_string piece_str in
         if grid_num >= 1 && grid_num <= 9 && piece_num >= 1 && piece_num <= 9 then
           if Board.is_valid board grid_num piece_num then (grid_num, piece_num)
           else begin print_endline "Illegal move."; loop () end
         else begin print_endline "Incorrect format"; loop () end
    | _ -> print_endline "Incorrect format"; loop ()
  in
  loop ()


let rec run () =
  (* set player name *)
  print_string "Enter player 1 name: ";
  let player_one = read_line () in
  if String.length player_one == 0 then (
    print_endline "Invalid username"; run ()
  )
  else
    print_string "Enter player 2 name: ";
  let player_two = read_line () in
  if String.length player_two == 0 then (
    print_endline "Invalid username"; run ()
  )
  else
    print_endline (player_one ^ " will be O. " ^ player_two ^ " will be X.\n");

  (* init board *)
  let board = Board.init in
  Board.print board;

  let rec loop i board =
    (* set current player value *)
    let (current_player, player_piece, player_grid) =
      if i mod 2 = 0 then (player_one, Piece.O, Grid.O)
      else (player_two, Piece.X, Grid.X)
    in

    (* get move *)
    print_endline ("\n" ^ current_player ^ "'s turn to play.");
    let (grid_num, piece_num) = parse board in

    (* fill board*)
    let new_board = Board.fill board grid_num piece_num player_piece current_player in
    print_char '\n';
    Board.print new_board;

    (* check winning condition *)
    if Board.check new_board player_grid then begin
        print_endline ("\n" ^ current_player ^ " wins the game!");
        print_endline "Starting new game.\n";
        run ()
      end
    else loop (i + 1) new_board
  in
  loop 0 board


let main () =
  run ()


let () = main ()
