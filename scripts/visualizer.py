def GenerateSkewPlot(skew_array, ruta_al_genoma):
    import matplotlib.pyplot as plt
    import os
    
    base_name = os.path.basename(ruta_al_genoma) 
    clean_name = os.path.splitext(base_name)[0] 

    plt.figure(figsize=(12, 6))
    plt.plot(skew_array, color='#1abc9c', label='Accumulated GC Skew')
    
    # Encontrar el mínimo del skew_array para marcarlo en el gráfico
    min_val = min(skew_array)
    min_pos = skew_array.index(min_val)

    plt.scatter(min_pos, min_val, color='red', s=100,zorder=5, label=f'Detected OriC ({min_pos} bp)')

    plt.title(f"Genomic Skew Analysis- {clean_name}")
    plt.xlabel("Genome Position (bp)")
    plt.ylabel("Skew Value")
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    output_filename = f"{clean_name}_analysis.png"
    plt.savefig(output_filename)
    print(f"Saved as: {output_filename}")
    plt.close()
