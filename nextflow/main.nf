nextflow.enable.dsl=2

process RUN_ORISCAN {
    container 'oriscan-image:latest'
    // Esto es vital: le dice a Nextflow que mueva los archivos finales a tu carpeta real
    publishDir "results", mode: 'copy' 

    input:
    path genome_file

    output:
    // Nextflow captura lo que aparezca en el directorio de trabajo del proceso
    path "*.png" 

    script:
    """
    python /app/main.py ${genome_file}
    """
}

workflow {
    // Busca todos los fasta en la carpeta raw
    genome_ch = channel.fromPath( 'data/raw/*.fasta' )
    RUN_ORISCAN(genome_ch)
}