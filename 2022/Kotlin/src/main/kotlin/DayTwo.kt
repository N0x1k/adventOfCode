import java.io.File

fun score(inputs: MutableList<String>){
    var score = 0

    inputs.forEach {
        when {
            it.contains("X") -> score += 1
            it.contains("Y") -> score += 2
            it.contains("Z") -> score += 3
        }
        when {
            it.contains(Regex("A X|B Y|C Z")) -> score += 3
            it.contains(Regex("A Y|B Z|C X")) -> score += 6
        }
    }
    println(score)
}

fun main(){
    // part one
    val inputs: MutableList<String> = mutableListOf()
    File("./inputs/2-full.txt").forEachLine {
        inputs.add(it)
    }
    score(inputs)

    // part two
    val resolvedInputs: MutableList<String> = mutableListOf()
    inputs.forEach {
        val (a,b) = Pair(it.substringBefore(" "), it.substringAfter(" "))
        when (a) {
            "A" -> {
                when (b) {
                    "X" -> resolvedInputs.add(it.replace(b, "Z"))
                    "Y" -> resolvedInputs.add(it.replace(b, "X"))
                    "Z" -> resolvedInputs.add(it.replace(b, "Y"))
                }
            }
            "B" -> resolvedInputs.add(it)
            "C" -> {
                when (b) {
                    "X" -> resolvedInputs.add(it.replace(b, "Y"))
                    "Y" -> resolvedInputs.add(it.replace(b, "Z"))
                    "Z" -> resolvedInputs.add(it.replace(b, "X"))
                }
            }
        }
    }
    score(resolvedInputs)
}