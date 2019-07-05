type t = O | X | Pieces of (Piece.t * Piece.t * Piece.t * Piece.t *Piece.t *Piece.t * Piece.t * Piece.t * Piece.t)


let init = Pieces (Piece.Empty, Piece.Empty, Piece.Empty, Piece.Empty, Piece.Empty, Piece.Empty, Piece.Empty, Piece.Empty, Piece.Empty)


let to_string_line (grid:t) (line:int) =
  match grid with
  | O when line = 0 -> "\\   /"
  | O when line = 1 -> "  O  "
  | O when line = 2 -> "/   \\"
  | X when line = 0 -> "\\   /"
  | X when line = 1 -> "  X  "
  | X when line = 2 -> "/   \\"
  | Pieces (a, b, c, _, _, _, _, _, _) when line = 0 ->
    (Piece.to_string a) ^ " " ^ (Piece.to_string b) ^ " " ^ (Piece.to_string c)
  | Pieces (_, _, _, a, b, c, _, _, _) when line = 1 -> 
    (Piece.to_string a) ^ " " ^ (Piece.to_string b) ^ " " ^ (Piece.to_string c)
  | Pieces (_, _, _, _, _, _, a, b, c) when line = 2 -> 
    (Piece.to_string a) ^ " " ^ (Piece.to_string b) ^ " " ^ (Piece.to_string c)
  | _ -> ""


let print (grid:t) =
  print_endline (to_string_line grid 0);
  print_endline (to_string_line grid 1);
  print_endline (to_string_line grid 2)


let is_valid grid piece_num =
  match grid with
  | O | X -> false
  | Pieces (a, b, c, d, e, f, g, h, i) ->
    if      piece_num = 1 && a <> Piece.Empty then false
    else if piece_num = 2 && b <> Piece.Empty then false
    else if piece_num = 3 && c <> Piece.Empty then false
    else if piece_num = 4 && d <> Piece.Empty then false
    else if piece_num = 5 && e <> Piece.Empty then false
    else if piece_num = 6 && f <> Piece.Empty then false
    else if piece_num = 7 && g <> Piece.Empty then false
    else if piece_num = 8 && h <> Piece.Empty then false
    else if piece_num = 9 && i <> Piece.Empty then false
    else true


let check grid value =
  match grid with
  | O | X -> true
  | Pieces (a, b, c, d, e, f, g, h, i) ->
    if      a = value && b = value && c = value then true
    else if d = value && e = value && f = value then true
    else if g = value && h = value && i = value then true
    else if a = value && d = value && g = value then true
    else if b = value && e = value && h = value then true
    else if c = value && f = value && i = value then true
    else if a = value && e = value && i = value then true
    else if c = value && e = value && g = value then true
    else false


let fill grid grid_num piece_num value player =
  let new_grid = 
    match grid with
    | Pieces (a, b, c, d, e, f, g, h, i) when piece_num = 1 -> Pieces (value, b, c, d, e, f, g, h, i)
    | Pieces (a, b, c, d, e, f, g, h, i) when piece_num = 2 -> Pieces (a, value, c, d, e, f, g, h, i)
    | Pieces (a, b, c, d, e, f, g, h, i) when piece_num = 3 -> Pieces (a, b, value, d, e, f, g, h, i)
    | Pieces (a, b, c, d, e, f, g, h, i) when piece_num = 4 -> Pieces (a, b, c, value, e, f, g, h, i)
    | Pieces (a, b, c, d, e, f, g, h, i) when piece_num = 5 -> Pieces (a, b, c, d, value, f, g, h, i)
    | Pieces (a, b, c, d, e, f, g, h, i) when piece_num = 6 -> Pieces (a, b, c, d, e, value, g, h, i)
    | Pieces (a, b, c, d, e, f, g, h, i) when piece_num = 7 -> Pieces (a, b, c, d, e, f, value, h, i)
    | Pieces (a, b, c, d, e, f, g, h, i) when piece_num = 8 -> Pieces (a, b, c, d, e, f, g, value, i)
    | Pieces (a, b, c, d, e, f, g, h, i) when piece_num = 9 -> Pieces (a, b, c, d, e, f, g, h, value)
    | _ -> grid
  in
  if check new_grid value = false then new_grid
  else if value = Piece.O then begin print_endline (player ^ " wins grid " ^ (string_of_int grid_num) ^ "!"); O end
  else begin print_endline (player ^ " wins grid " ^ (string_of_int grid_num) ^ "!"); X end
